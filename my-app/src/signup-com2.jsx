import './SignUp-company-2.css';

const Signupcom2 = (props) =>{
    return(
        <div>
            
            <div className="container">
            
                <div className="card py-5 px-3 g-2">
                <label className="location text-center">ที่อยู่ของบริษัท</label> 
                    <div className="group1 input-group d-flex flex-row mt-2 gap-4 mb-4 justify-content-center align-items-center">
                        <input type="text" className="baan" placeholder=" ที่อยู่" />
                    </div>
                    <div className="group3 input-group d-flex flex-row mt-2 gap-4 mb-4 justify-content-center align-items-center">
                        <input type="text" className="o" placeholder=" รหัสไปรษณีย์" />
                    </div>
                    
                    <a
                    href="Sign Up-company-3.html"
                    className="btn btn-success justify-content-center align-items-center"
                    type="submit"
                    >
                    ต่อไป
                    </a>
                    <p className="help2 text-center">ต้องการความช่วยเหลือ?</p>
        </div>
    </div>

        </div>
    )
}
export default Signupcom2