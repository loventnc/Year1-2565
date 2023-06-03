import homework from '../src/image/homework.png'
import clockk from '../src/image/clockk.png'
import { DataMonther, DataNumber, DataTime} from '../src/data/Datadate'
import { dataWork } from './data/dataWork'
import axios from 'axios'
import { useEffect,useState,Dispatch } from 'react'

const Homework = () => {


    const baseURL = 'http://localhost:3000/homewrk/create'
    const [data, Setdata] = useState([])
    const [namework, Setnamework] = useState('')
    const [day, Setday] = useState(0)
    const [month, Setmonth] = useState(0)
    const [hour, Sethour] = useState(0)
    const [minute, Setminute] = useState(0)

    useEffect(() => {
        axios.get(baseURL).then((response) => {
            console.log(response.data);
            Setdata(response.data)
        }).catch(err =>console.log(err))
    }, [])

    const postData = (e) => {
        e.preventDefault();
        axios.post(baseURL, {
            namework,day,month,hour,minute
        }).then(response => console.log('Postting',response)).catch(err => console.log(err))}

        console.log(namework);

    return (
        <>
            <div className='bg-[#AFD3E2] h-screen'>
                <div className='container mx-auto px-[5px]'>
                    <div className='pt-10 rounded-lg '>
                        <h1 className='text-[24px] bg-[#19A7CE] text-white px-10 py-2'>HOMEWORK</h1>
                    </div>
                    <div>
                        <div className='flex justify-center'>
                            <div className='flex justify-between w-full container mx-auto px-[220px]'>
                                <div className='flex flex-col'>
                                    <div className='flex'>
                                        <h2 className='text-[20px] pt-10 '>Subject:</h2>
                                        <img src={homework} alt="" width="50px" className='pt-6 pl-2' />
                                    </div>
                                    <input type="text" value={namework} onChange={(e)=> Setnamework(e.target.value)} className='rounded-lg w-[300px] h-[30px] mt-7' />
                                </div>
                                <div className='flex flex-col'>
                                    <div className='flex'>
                                        <h2 className='text-[20px] pt-10 '>Deadline:</h2>
                                        <img src={clockk} alt="" width="50px" className='pt-6 pl-2' />
                                    </div>
                                    <td>
                                        <h5 className='text-[18px] mt-7'>Day: </h5>
                                        <select onChange={(e)=> Setday(e.target.value)} className='rounded-lg w-[300px] h-[30px] mt-3' value={day}>
                                            {dataWork.map((item, id) => {
                                                return (
                                                    <option key={id} value={item}>{item}</option>
                                                )
                                            })}
                                        </select>
                                    </td>
                                    <td>
                                        <h6 className='text-[18px] mt-5'>Month: </h6>
                                        <select className='rounded-lg w-[300px] h-[30px] mt-3' onChange={(e)=>Setmonth(e.target.value)} value={month}>
                                            {DataMonther.map((item, id) => {
                                                return (
                                                    <option key={id} value={item}>{item}</option>
                                                )
                                            })}
                                        </select>
                                    </td>
                                    <td>
                                        <h6 className='text-[18px] mt-5'>Time: </h6>
                                        <select className='rounded-lg w-[300px] h-[30px] mt-3' onChange={(e)=>Sethour(e.target.value)} value={hour}>
                                            {DataTime.map((item, id) => {
                                                return (
                                                    <option key={id} value={item} >{item}</option>
                                                )
                                            })}
                                        </select>
                                    </td>
                                    <td>
                                        <select className='rounded-lg w-[300px] h-[30px] mt-3'  onChange={(e)=>Setminute(e.target.value)} value={minute}>
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
                            <button className='text-[16px] bg-[#19376D] text-white px-10 py-1 rounded-lg'type='summit' onClick={postData}>SUMMIT</button>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Homework