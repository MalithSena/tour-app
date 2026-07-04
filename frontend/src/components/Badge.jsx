function Badge({ children }) {
  return (
    <span style={{
      fontFamily: "'IBM Plex Mono', monospace",
      fontSize: '11px',
      letterSpacing: '0.06em',
      textTransform: 'uppercase',
      color: 'var(--rust)',
      border: '1px solid var(--rust)',
      padding: '6px 12px',
      borderRadius: '3px',
      display: 'inline-block',
    }}>
      {children}
    </span>
  );
}

export default Badge;