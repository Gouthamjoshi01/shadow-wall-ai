import React, { useState, useEffect } from 'react';
import { Shield, ShieldAlert, ShieldCheck, Activity } from 'lucide-react';

export default function App() {
  const [logs, setLogs] = useState([]);
  const [stats, setStats] = useState({ total: 0, blocked: 0, allowed: 0 });

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8000/ws/logs');

    ws.onmessage = (event) => {
      const log = JSON.parse(event.data);
      setLogs((prev) => [log, ...prev.slice(0, 49)]);
      setStats((prev) => ({
        total: prev.total + 1,
        blocked: prev.blocked + (log.blocked ? 1 : 0),
        allowed: prev.allowed + (log.blocked ? 0 : 1),
      }));
    };

    return () => ws.close();
  }, []);

  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 p-6 font-sans">
      <header className="flex items-center space-x-3 mb-8 border-b border-slate-800 pb-4">
        <Shield className="w-8 h-8 text-indigo-400" />
        <h1 className="text-2xl font-bold tracking-wide">ShadowWall AI // Real-Time Threat Intelligence</h1>
      </header>

      {/* Metrics Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div className="bg-slate-800 p-5 rounded-lg border border-slate-700 flex items-center justify-between">
          <div>
            <p className="text-slate-400 text-sm font-medium">Total Requests</p>
            <p className="text-3xl font-extrabold mt-1">{stats.total}</p>
          </div>
          <Activity className="w-8 h-8 text-blue-400 opacity-80" />
        </div>

        <div className="bg-slate-800 p-5 rounded-lg border border-slate-700 flex items-center justify-between">
          <div>
            <p className="text-slate-400 text-sm font-medium">Threats Blocked</p>
            <p className="text-3xl font-extrabold text-red-400 mt-1">{stats.blocked}</p>
          </div>
          <ShieldAlert className="w-8 h-8 text-red-400 opacity-80" />
        </div>

        <div className="bg-slate-800 p-5 rounded-lg border border-slate-700 flex items-center justify-between">
          <div>
            <p className="text-slate-400 text-sm font-medium">Allowed Traffic</p>
            <p className="text-3xl font-extrabold text-emerald-400 mt-1">{stats.allowed}</p>
          </div>
          <ShieldCheck className="w-8 h-8 text-emerald-400 opacity-80" />
        </div>
      </div>

      {/* Live Logs Table */}
      <div className="bg-slate-800 rounded-lg border border-slate-700 p-4">
        <h2 className="text-lg font-semibold mb-4 text-slate-200">Live Traffic Feed</h2>
        <div className="overflow-x-auto">
          <table className="w-full text-left text-sm">
            <thead className="bg-slate-900/50 text-slate-400">
              <tr>
                <th className="p-3">Status</th>
                <th className="p-3">Method</th>
                <th className="p-3">Path</th>
                <th className="p-3">Threat Type</th>
                <th className="p-3">Payload Preview</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-700/50">
              {logs.map((log, index) => (
                <tr key={index} className="hover:bg-slate-700/30">
                  <td className="p-3">
                    <span className={`px-2.5 py-1 rounded-full text-xs font-semibold ${log.blocked ? 'bg-red-500/20 text-red-400' : 'bg-emerald-500/20 text-emerald-400'}`}>
                      {log.blocked ? 'BLOCKED 403' : 'ALLOWED 200'}
                    </span>
                  </td>
                  <td className="p-3 font-mono text-slate-300">{log.method}</td>
                  <td className="p-3 font-mono text-slate-300">{log.path}</td>
                  <td className="p-3 text-slate-300">{log.threat_type}</td>
                  <td className="p-3 font-mono text-slate-400 text-xs truncate max-w-xs">{log.payload || '-'}</td>
                </tr>
              ))}
              {logs.length === 0 && (
                <tr>
                  <td colSpan="5" className="text-center p-6 text-slate-500">Waiting for live traffic requests...</td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
