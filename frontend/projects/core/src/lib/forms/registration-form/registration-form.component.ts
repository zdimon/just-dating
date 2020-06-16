
import { Component, OnInit } from '@angular/core';
import { ApiService } from './../../services/api.service';

@Component({
  selector: 'core-registration-form',
  templateUrl: './registration-form.component.html',
  styleUrls: ['./registration-form.component.scss']
})
export class RegistrationFormComponent implements OnInit {

  name = '';
  email = '';
  password = '';
  gender = '';
  birthday = '';

  constructor(private api: ApiService) { }

  ngOnInit() {
  }


  submit() {
    const data = {
      username: this.name,
      password: this.password,
      gender: this.gender,
      email: this.email,
      birthday: this.birthday
    }
    this.api.registration(data).subscribe(rez => {
      console.log(rez);
    });
  }
}
