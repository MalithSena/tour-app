import { useState, useEffect } from 'react';

function Expertise() {
  const [destinations, setDestinations] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/destinations/')
      .then((res) => res.json())
      .then((data) => {
        setDestinations(data);
        setLoading(false);
      });
  }, []);

  if (loading) return <p style={{ padding: '60px', fontFamily: 'sans-serif' }}>Loading...</p>;

  return (
    <div style={{ maxWidth: '700px', margin: '0 auto', padding: '60px 20px', fontFamily: 'sans-serif' }}>
      <h1>Areas of Expertise</h1>
      <p style={{ color: '#666' }}>
        Regions across Sri Lanka where I've guided extensively over the past 15+ years.
      </p>

      {destinations.map((dest) => (
        <div key={dest.id} style={{ marginTop: '32px', borderTop: '1px solid #ddd', paddingTop: '20px' }}>
          <h2>{dest.name}</h2>
          <p style={{ color: '#888', fontSize: '14px', textTransform: 'uppercase' }}>
            {dest.location} · {dest.category}
          </p>
          <p>{dest.description}</p>
        </div>
      ))}
    </div>
  );
}

export default Expertise;