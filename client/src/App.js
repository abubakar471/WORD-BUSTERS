import {BrowserRouter, Routes, Route} from "react-router-dom"
import Game from "./pages/Game"

const App = () => {
  return(
    <BrowserRouter>
    <Routes>
      <Route path="/game" element={<Game />} />
    </Routes>
    </BrowserRouter>
  )
}

export default App