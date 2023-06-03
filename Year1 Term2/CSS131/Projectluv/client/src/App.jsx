import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Menubar from './components/Menubar'
import Homepage from './Homepage'
import Class from './Class'
import Homework from './Homework'
import Check from './Check'
import Contact from './Contact'

import { Route, Routes } from 'react-router-dom'

function App() {
 

  return (
    <>
    <Menubar/>
    <Routes>
      <Route path='/' element={<Homepage/>}/>
      <Route path='/class' element={<Class/>}/>
      <Route path='/homework' element={<Homework/>}/>
      <Route path='/check' element={<Check/>}/>
      <Route path='/contact' element={<Contact/>}/>
    

    </Routes>
    </>
  )
}

export default App
