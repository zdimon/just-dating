import { Component } from '@angular/core';
import {ApiService} from '../../../core/src/lib/services/api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  users = [];
  constructor(private apiService: ApiService){
    this.apiService.getUserList().subscribe((data: any) => {
      this.users = data;
    });
  }
}
