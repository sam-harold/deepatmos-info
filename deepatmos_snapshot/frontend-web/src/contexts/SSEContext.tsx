"""SSE Context — high-performance real-time state management for web dashboard."""

import React, { useEffect, useState, useRef, useCallback } from 'react';
# [REDACTED: sensitive imports and types]

interface SSEProviderProps {
  children: React.ReactNode;
}

export const SSEProvider: React.FC<SSEProviderProps> = ({ children }) => {
  const [incidents, setIncidents] = useState<any[]>([]);
  const [isConnected, setIsConnected] = useState(false);
  const [isReconnecting, setIsReconnecting] = useState(false);
  
  const accessToken = useAuthStore((state) => state.accessToken);
  const eventSourceRef = useRef<EventSource | null>(null);
  const retryCountRef = useRef(0);
  const pendingIncidentsRef = useRef<any[]>([]);
  const incidentBatchTimerRef = useRef<any>(null);

  /**
   * High-Efficiency Batching & State Updates
   * 
   * Logic Flow:
   * 1. Collect incoming incidents in an in-memory queue (pendingIncidentsRef).
   * 2. Schedule a batch flush (e.g., every 250ms on Chrome).
   * 3. Deduplicate and merge updates within the batch (upsertIncident logic).
   * 4. Perform a single React state update to minimize re-renders.
   */
  const flushPendingIncidents = useCallback(() => {
    const batch = pendingIncidentsRef.current;
    pendingIncidentsRef.current = [];
    
    // [REDACTED: sensitive batch deduplication and upsert logic]
    setIncidents((prev) => /* merge batch into state */ []);
    
    // Notify the user via toast notifications (rate-limited)
    // [REDACTED: sensitive toast dedup/cooldown logic]
  }, []);

  /**
   * Robust Connection Lifecycle Management
   * 
   * Logic Flow:
   * 1. On mount (or token change), initialize EventSource connection.
   * 2. Handle onopen to reset retry counters.
   * 3. Handle onerror with exponential backoff and automatic JWT refresh.
   * 4. Handle onmessage to hydrate the pending queue.
   * 5. Clean up connection and timers on unmount.
   */
  useEffect(() => {
    if (!accessToken) return;

    const connect = (token: string) => {
      // [REDACTED: sensitive EventSource endpoint with token hydration]
      const source = new EventSource(/* ... */);
      eventSourceRef.current = source;

      source.onmessage = (event) => {
        // [REDACTED: sensitive message parsing and batching triggers]
      };

      source.onerror = () => {
        // [REDACTED: sensitive exponential backoff and refreshAccessToken() logic]
      };
    };

    connect(accessToken);
    return () => cleanup();
  }, [accessToken]);

  return (
    <IncidentContext.Provider value={{ incidents, isConnected, isReconnecting }}>
      {children}
    </IncidentContext.Provider>
  );
};
