// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import {getFirestore} from 'firebase/firestore';
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAWIBER9XfKa8xA70Teu443EYZrdqFS_b0",
  authDomain: "studyal-41622.firebaseapp.com",
  databaseURL: "https://studyal-41622-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "studyal-41622",
  storageBucket: "studyal-41622.appspot.com",
  messagingSenderId: "250984246707",
  appId: "1:250984246707:web:4644eda7020d8f691a6fc6",
  measurementId: "G-SJ99QS5FP7"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);
const analytics = getAnalytics(app);