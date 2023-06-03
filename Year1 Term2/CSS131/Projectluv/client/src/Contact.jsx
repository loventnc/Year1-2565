import React from 'react'
import me from '../src/image/me.jpg'

const Contact = () => {
  return (
    <div className='bg-[#AFD3E2] h-screen'>
      <div className='pt-10 container mx-auto px-[5px]'>
        <h1 className='text-[24px] bg-[#19A7CE] text-white px-10 py-2'>CONTACT</h1>
          <div className='flex items-center justify-between container mx-auto px-[200px]'>
          <img src={me} alt="" width="250px" className='pt-10' />
            <div className='border rounded-lg bg-[#BFDCE5] text-[20px] px-[70px] pl-10 pt-5 pb-5'>
              <h5>Student ID: 65090500435</h5>
              <h1 className='mt-3'>Name: Nattanischa Aumpornchairuch</h1>
              <h3 className='mt-3'>Telephone number: 061-6166491</h3>
              <h4 className='mt-3 '>Facebook: Nattanischa Aumpornchairuch</h4>
            </div>
          </div>
      </div>
    </div>
  )
}

export default Contact