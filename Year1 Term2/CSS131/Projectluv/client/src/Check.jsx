// import React from 'react'
import openbook from '../src/image/openbook.png'
import homework from '../src/image/homework.png'
import { useEffect, useState } from 'react'
import axios from 'axios'

export const Check = () => {

    const baseURLWork = 'http://localhost:3000/homewrk'
    const baseURLClass = 'http://localhost:3000/classschedule'

    const [dataClass, setDataClass] = useState([])
    const [dataWork, setDataWork] = useState([])

    async function fetchDataClass() {
        const response = await axios.get(baseURLClass)
        setDataClass(response.data)
    }
    async function fetchDataWork() {
        const response = await axios.get(baseURLWork)
        setDataWork(response.data)
    }
    useEffect(() => {
        fetchDataClass()
        fetchDataWork()
    }, [dataClass, dataWork])



    return (
        <>
            <div className='bg-[#AFD3E2] h-screen'>
                <div className='container mx-auto px-[5px]'>
                    <div className='pt-10 rounded-lg '>
                        <h1 className='text-[24px] bg-[#19A7CE] text-white px-10 py-2'>CHECK</h1>
                    </div>
                    <div className='flex justify-center flex-row gap-96'>
                        <div>
                            <div>
                                <div className='flex'>
                                    <h2 className='text-[20px] pt-10 '>CLASS SCHEDULE:</h2>
                                    <img src={openbook} alt="" width="50px" className='pt-6 pl-2' />
                                </div>
                                {dataClass.map((item, index) => {
                                    return (
                                        <div key={index}>
                                            <h1>{item.namesubject}</h1>
                                            <h1>{item.classsite}</h1>
                                            <h1>{item.day}</h1>
                                            <h1>{item.time}:{item.mintime}</h1>
                                        </div>
                                    )
                                })}
                            </div>
                        </div>
                        <div>
                            <div className='flex'>
                                <h3 className='text-[20px] pt-10'>HOMEWORK:</h3>
                                <img src={homework} alt="" width="50px" className='pt-6 pl-2' />
                            </div>
                            {dataWork.map((item, index) => {
                                return(
                                    <div key={index}>
                                        <h1>{item.namework}</h1>
                                        <h1>{item.day}</h1>
                                        <h1>{item.month}</h1>
                                        <h1>{item.hour}:{item.mintime}</h1>
                                    </div>
                                )
                            })
                                
                            }
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Check