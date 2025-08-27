import React, {useEffect, useState} from 'react'

export default function App() {
  const [providers, setProviders] = useState([])
  const [rankings, setRankings] = useState([])

  useEffect(()=> {
    fetch('/providers?limit=10')
      .then(r=>r.json())
      .then(setProviders)
      .catch(console.error)
    fetch('/rankings?top=10')
      .then(r=>r.json())
      .then(setRankings)
      .catch(console.error)
  },[])

  return (
    <div style={{fontFamily:'Arial, sans-serif', padding:20}}>
      <h1>Health Transparency — Demo Dashboard</h1>
      <section>
        <h2>Top Providers by Mean Allowed Charge</h2>
        <ol>
          {rankings.map(r=> <li key={r.npi}>{r.provider_name} — ${Number(r.mean_avg_allowed).toFixed(2)}</li>)}
        </ol>
      </section>
      <section>
        <h2>Providers (sample)</h2>
        <ul>
          {providers.map(p=> <li key={p.npi}>{p.provider_name} ({p.state})</li>)}
        </ul>
      </section>
    </div>
  )
}
