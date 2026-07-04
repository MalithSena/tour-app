import { useState, useEffect } from 'react';

function Seal() {
  const [photoUrl, setPhotoUrl] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/profile/')
      .then((res) => res.json())
      .then((data) => {
        if (data.length > 0) {
          setPhotoUrl(data[0].photo);
        }
      })
      .catch((err) => console.error('Failed to load profile photo:', err));
  }, []);

  return (
    <div style={{
      width: '190px',
      height: '190px',
      borderRadius: '50%',
      border: '1.5px solid var(--gold)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      background: 'rgba(201,154,59,0.06)',
      flexShrink: 0,
      padding: '10px',
    }}>
      <div style={{
        width: '154px',
        height: '154px',
        borderRadius: '50%',
        border: '1px dashed rgba(201,154,59,0.6)',
        overflow: 'hidden',
        position: 'relative',
        background: 'rgba(0,0,0,0.15)',
      }}>
        {photoUrl && (
          <img
            src={photoUrl}
            alt="Malith Senanayake"
            style={{
              width: '100%',
              height: '100%',
              objectFit: 'cover',
            }}
          />
        )}
        <div style={{
          position: 'absolute',
          bottom: 0,
          left: 0,
          right: 0,
          background: 'rgba(20,42,31,0.85)',
          padding: '6px 4px',
          textAlign: 'center',
        }}>
          <span style={{
            fontFamily: "'IBM Plex Mono', monospace",
            fontSize: '9px',
            letterSpacing: '0.05em',
            color: 'var(--gold-bright)',
          }}>NATIONAL GUIDE · SRI LANKA</span>
        </div>
      </div>
    </div>
  );
}

export default Seal;