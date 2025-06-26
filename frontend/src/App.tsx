import React, { useState, useEffect } from 'react'

interface HealthStatus {
  status: string
  database: string
}

function App() {
  const [health, setHealth] = useState<HealthStatus | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const checkHealth = async () => {
      try {
        const response = await fetch('http://localhost:8000/health')
        const data = await response.json()
        setHealth(data)
      } catch (error) {
        console.error('Health check failed:', error)
        setHealth({ status: 'error', database: 'disconnected' })
      } finally {
        setLoading(false)
      }
    }

    checkHealth()
  }, [])

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>POC TaskMaster</h1>
      <p>A modern task management application</p>
      
      <div style={{ marginTop: '20px' }}>
        <h2>System Status</h2>
        {loading ? (
          <p>Checking system health...</p>
        ) : (
          <div>
            <p>API Status: <strong>{health?.status || 'unknown'}</strong></p>
            <p>Database: <strong>{health?.database || 'unknown'}</strong></p>
          </div>
        )}
      </div>

      <div style={{ marginTop: '20px' }}>
        <h2>Features</h2>
        <ul>
          <li>SQLite database with WAL mode</li>
          <li>FastAPI backend with dependency injection</li>
          <li>React + TypeScript frontend</li>
          <li>Vitest for testing</li>
        </ul>
      </div>
    </div>
  )
}

export default App