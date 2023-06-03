import group from '../src/image/group.png'
import calender from '../src/image/calendar.png'
import search from '../src/image/search.png'

const Homepage = () => {

  
  return (
    <>
    <div className="bg-[#AFD3E2] h-screen">
      <div className='flex flex-col justify-center items-center h-[600px]'>
        <h1 className='text-[40px] '>Time Reminder for Study</h1>
        <h2 className='text-[20px]'>Reminder for study time, activities, and homework submissions  via LINE</h2>
        <div className='flex justify-center gap-5 rounded-lg mt-[70px]'>
          <img src={group} alt="" width="50px" />
          <button className='text-[20px] bg-[#19A7CE] text-white px-10 py-2 rounded-lg hover:bg-[#7C96AB]'><a href="/Class">PUT SCHEDULE</a></button>
          <button className='text-[20px] bg-[#19A7CE] text-white px-10 py-2 rounded-lg hover:bg-[#7C96AB]'><a href="/Homework">PUT HOMEWORK </a></button>
          <img src={calender} alt="" width="50px" />
        </div>
        <div className='flex justify-center mt-5'>
            <button className='text-[20px] bg-[#19A7CE] text-white px-10 py-2 rounded-lg hover:bg-[#7C96AB]'><a href="/Check">CHECK</a></button> 
          </div>
          <img className='pt-5' src={search} alt="" width="50px" />
      </div>
    </div>
    </>
  )
}

export default Homepage