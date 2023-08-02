import './SignUp-company-1.css';

const Signupcom1 = (props) =>{
    return(
        <div>
            <div className="container min-vh-100 d-flex justify-content-center align-items-center">
            <div className="card py-5 px-3">
            <h1 className="text-center" id="Create_Name">
                สร้างบัญชีบริษัท
            </h1>
            <div className="input-group d-flex flex-column mt-2 gap-4 mb-4">
                <input
                type="text"
                className="username align-items-center"
                placeholder="   ชื่อบริษัท"
                />
                <input
                type="email"
                className="email align-items-center"
                placeholder="   อีเมล"
                />
                <input
                type="tel"
                className="tel align-items-center"
                placeholder="   เบอร์โทร"
                />
            </div>
            <button className="next col-2" href="Sign Up-company-2.html">
                ต่อไป
            </button>
            <p className="help2 text-center">ต้องการความช่วยเหลือ?</p>
            </div>
        </div>
      </div>
    )
}

export default Signupcom1;