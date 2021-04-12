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

  registration(data: any) {
    return this.http.post(`${environment.backendUrl}v1/account/registration`, data);
  }

  login(data: any) {
    return this.http.post(`${environment.backendUrl}v1/account/login`, data);
  }

  logout() {
    return this.http.get(`${environment.backendUrl}v1/account/logout`);
  }


  getChatRoom(userId: number) {
    return this.http.get(`${environment.backendUrl}v1/chat/get_room/${userId}`);
  }

  getChatMessage(roomId: string) {
    return this.http.get(`${environment.backendUrl}v1/chat/get_room_messages?token=${roomId}`);
  }

  sendMessage(data: any) {
    return this.http.post(`${environment.backendUrl}v1/chat/create_message/`, data);
  }

  sendQuizMessage(data: any) {
    return this.http.post(`${environment.backendUrl}v1/quiz/save_message/`, data);
  }

  getQuizMessage(roomId: string) {
    return this.http.get(`${environment.backendUrl}v1/quiz/get_room_messages/${roomId}`);
  }


}
