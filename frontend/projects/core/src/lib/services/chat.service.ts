
import { Injectable } from '@angular/core';

import { ApiService } from './api.service';
import { Router } from '@angular/router';

// Store
import { Store } from '@ngrx/store';
import * as chatRoomActions from './../../store/actions/chat-room.action';
import { ChatRoomState } from './../../store/states/chat-room.state';
import * as chatMessageActions from './../../store/actions/chat-message.action';
import { ChatMessageState } from './../../store/states/chat-message.state';

@Injectable({
  providedIn: 'root'
})
export class ChatService {

  constructor(
    private api: ApiService,
    private router: Router,
    private chatRoomStore: Store<ChatRoomState>,
    private chatMessageStore: Store<ChatMessageState>,
    ) { }

  getChatRoom(userId: number){
    this.api.getChatRoom(userId).subscribe((data: any) => {
      console.log(data);
      this.chatRoomStore.dispatch(new chatRoomActions.UpdateChatRoom(data));
      this.router.navigate(['chat/' + data.token]);
    })
  }

  getChatMessage(roomId: string){
    this.api.getChatMessage(roomId).subscribe((data: any) => {
      console.log(data);
      this.chatMessageStore.dispatch(new chatMessageActions.UpdateChatMessages(data.payload));
    })
  }

  sendChatMessage(data: any) {
    this.api.sendMessage(data).subscribe((rez: any) => {
    })
  }


}
