const photos = [
  { src: '/gallery/photo1.jpeg', caption: 'Guiding a group at Polonnaruwa' },
  { src: '/gallery/photo2.jpeg', caption: 'Boat ride in Madu River' },
  { src: '/gallery/photo3.jpeg', caption: 'Cooking with Chef' },
];

function Gallery() {
  return (
    <div style={{ maxWidth: '900px', margin: '0 auto', padding: '60px 20px', fontFamily: 'sans-serif' }}>
      <h1>Gallery</h1>
      <p style={{ color: '#666' }}>
        Life on the road and at home — fifteen years of guiding, and the farm in between.
      </p>

      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))',
        gap: '16px',
        marginTop: '30px'
      }}>
        {photos.map((photo, index) => (
          <div key={index}>
            <img
              src={photo.src}
              alt={photo.caption}
              style={{ width: '100%', height: '220px', objectFit: 'cover', borderRadius: '4px' }}
            />
            <p style={{ fontSize: '13px', color: '#888', marginTop: '6px' }}>{photo.caption}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Gallery;