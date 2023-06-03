import openbook from '../src/image/openbook.png'
import schedule from '../src/image/schedule.png'
import { Datadate, DataTime, Sitelearn, DataNumber } from '../src/data/Datadate'
import axios from 'axios'
import { useEffect, useState } from 'react'

const Class = () => {

    const baseURL = 'http://localhost:3000/classschedule/create'

    const [data, setData] = useState([])
    const [namesubject, setNamesubject] = useState('')
    const [classsite, setClasssite] = useState('')
    const [day, setDay] = useState('')
    const [time, setTime] = useState('')
    const [mintime, setMintime] = useState(0)

    async function getDataClass() {
        axios.get(baseURL).then((response) => {
            console.log(response.data);
            setData(response.data)
        }).catch(err => console.log(err))
    }
    useEffect(() => {
        getDataClass()
    }, [])

    const handleSubmit = (e) => {
        e.preventDefault()
        const data = {
            namesubject: namesubject,
            classsite: classsite,
            day: day,
            time: time,
            mintime: mintime
        }
        axios.post(baseURL, data).then((response) => {
            console.log(response.data);
            getDataClass()
        }).catch(err => console.log(err))
    }

    return (
        <>
            <div className='bg-[#AFD3E2] h-screen'>
                <div className='container mx-auto px-[5px]'>
                    <div className='pt-10 rounded-lg '>
                        <h1 className='text-[24px] bg-[#19A7CE] text-white px-10 py-2'>CLASS SCHEDULE</h1>
                    </div>
                    <div>
                        <div className='flex justify-center'>
                            <div className='flex justify-between w-full container mx-auto px-[220px]'>
                                <div className='flex flex-col'>
                                    <div className='flex'>
                                        <h2 className='text-[20px] pt-10 '>Subject code/name:</h2>
                                        <img src={openbook} alt="" width="50px" className='pt-6 pl-2' />
                                    </div>
                                    <input type="text" className='rounded-lg w-[300px] h-[30px] mt-7' onChange={(e) => setNamesubject(e.target.value)} />
                                    <td>
                                        <select onChange={(e)=>setClasssite(e.target.value)}>
                                            {Sitelearn.map((item, id) => {
                                                return (
                                                    <option key={id} value={item.title}>{item.title}</option>
                                                )
                                            })}
                                        </select>
                                    </td>
                                </div>
                                <div className='flex flex-col'>
                                    <div className='flex'>
                                        <h2 className='text-[20px] pt-10 '>Class schedule:</h2>
                                        <img src={schedule} alt="" width="50px" className='pt-6 pl-2' />
                                    </div>
                                    <td>
                                        <select className='rounded-lg w-[300px] h-[30px] mt-7' onChange={(e) => setDay(e.target.value)} value={day}>
                                            {Datadate.map((item, id) => {
                                                return (
                                                    <option key={id} value={item.datevalue}>{item.date}</option>
                                                )
                                            })}
                                        </select>
                                    </td>
                                    <td>
                                        <select className='rounded-lg w-[300px] h-[30px] mt-7' onChange={(e) => setTime(e.target.value)} value={time}>
                                            {DataTime.map((item, id) => {
                                                return (
                                                    <option key={id} value={item}>{item}</option>
                                                )
                                            })}
                                        </select>
                                    </td>
                                    <td>
                                        <select className='rounded-lg w-[300px] h-[30px] mt-7' onChange={(e) => setMintime(e.target.value)} value={mintime}>
                                            {DataNumber.map((item, id) => {
                                                return (
                                                    <option key={id} value={item}>{item}</option>
                                                )
                                            })}
                                        </select>
                                    </td>
                                </div>
                            </div>
                        </div>
                        <div className='flex justify-center gap-5 rounded-lg mt-[70px]'>
                            <button type='summit' className='text-[16px] bg-[#19376D] text-white px-10 py-1 rounded-lg' onClick={handleSubmit}>SUMMIT</button>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Class