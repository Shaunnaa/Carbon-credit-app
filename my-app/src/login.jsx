import './login.css';
import img1 from './photo/tree.png';


const Login = (props) =>{
    return(
        <div>
    <div className="container mt-5 pt-5">
      <div className="col-12  col-sm-8 col-md-6 m-auto">
        <div className="card py-5 px-3">
          <h1 className="text-center" id="Create_Name">
            เข้าสู่ระบบ
          </h1>
          <div className="input-group d-flex flex-column mb-5">
          <label >อีเมล</label>
            <div className="form-floating">
              <input
                type="email"
                className="email form-control" placeholder="name@example.com"
              />
              
            </div>
            <label>รหัสผ่าน</label>
            <div className="form-floating">
              <input
                type="password"
                className="tel form-control"
                placeholder="name@example.com"
              />
              
            </div>
          </div>
          <button
            className="next"
            onclick="location.href='Sign Up-company-2.html'">
            เข้าสู่ระบบ
          </button>
          <button className="f text-center">จำรหัสผ่านไม่ได้</button>
        </div>
      </div>
    
  </div>
  <div className="container-fluid">
    <img className="img" src={img1} alt="tree"></img>
    </div>
        </div>
    )
}

export default Login