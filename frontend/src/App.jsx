import { Routes, Route } from 'react-router-dom';
import Nav from './components/Nav';
import Bio from './pages/Bio';
import Expertise from './pages/Expertise';
import Gallery from './pages/Gallery';

function App() {
  return (
    <div>
      <Nav />
      <Routes>
        <Route path="/" element={<Bio />} />
        <Route path="/expertise" element={<Expertise />} />
        <Route path="/gallery" element={<Gallery />} />
      </Routes>
    </div>
  );
}

export default App;