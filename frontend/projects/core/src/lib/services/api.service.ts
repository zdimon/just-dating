import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {environment} from '../../environments/environment';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }

  getUserList() {
    return this.http.get(`${environment.backendUrl}v1/account/user_list`).pipe(
      map((rez: any) => rez.payload)
    );
  }
}
