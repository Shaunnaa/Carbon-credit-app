import React from 'react'
import './buypage.css';
import img1 from './photo/Group 11.png';
function Buypage() {
  return (
    <div class="container  justify-content-center align-items-center">
    <section class="x  justify-content-center align-items-center">
        <img src={img1} class="img-circle justify-content-center align-items-center" ></img>
        <div class="card  mt-5 w-100">
            <div class="card-body d-flex justify-content-center align-items-center mb-1 mt-5">
                <div class="nemae">
                    <h5 class="connect-text">   จำนวนหน่วย</h5>
                    <input type="number" class="amount-lg align-items-center" value="1" min="1" max="2000" placeholder="   xxx"/>
                </div>               
            </div>
            <div class="card-body d-flex justify-content-center align-items-center mb-5">
                <div class="nemae">
                    <h1 class="connect-text"> ราคา(...)</h1>
                    <div class="cost align-items-center"></div>
                </div>
            </div>
            
           
            <div class="d-grid gap-1 col-2 mx-auto mb-5">
            <a  href="connecttopay.html" class="btn btn-success text-center" type="submit">ต่อไป</a>
          </div>
            
        </div>
    </section></div>
  )
}

export default Buypage