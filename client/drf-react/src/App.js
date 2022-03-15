
import {Route, Routes, Navigate} from 'react-router-dom'
import HomeView from './views/Home';
import LoginView from './views/Login'
import RegisterView from './views/Register'


function App() {


  return (
      <Routes>
          <Route path='/' exact element={ <HomeView />}></Route>
          <Route path='/login' exact element={ <LoginView />}></Route>
          <Route path='/register' exact element={ <RegisterView />}></Route>
          <Route path='*' element={<Navigate to='/' />}></Route>
      </Routes>
  );
}

export default App;