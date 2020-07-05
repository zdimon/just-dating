
import { Injectable } from '@angular/core';

import { ApiService } from './api.service';
import { Router } from '@angular/router';

// Store
import { Store } from '@ngrx/store';
import * as chatRoomActions from './../../store/actions/chat-room.action';
import { ChatRoomState } from './../../store/states/chat-room.state';


@Injectable({
  providedIn: 'root'
})
export class ChatService {

  constructor(
    private api: ApiService,
    private router: Router,
    private chatRoomStore: Store<ChatRoomState>,
    ) { }

  getChatRoom(userId: number){
    this.api.getChatRoom(userId).subscribe((data: any) => {
      console.log(data);
      this.chatRoomStore.dispatch(new chatRoomActions.UpdateChatRoom(data));
      this.router.navigate(['chat/' + data.token]);
    })
  }
}
