
import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import { ChatService } from './../../../../../core/src/lib/services/chat.service';

import { Store } from '@ngrx/store';
import { selectChatMessageByTokenSelector } from './../../../../../core/src/store/selectors/chat.selector';
import { ChatMessageListState } from './../../../../../core/src/store/states/chat-message.state';



@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss']
})
export class ChatComponent implements OnInit {

  token: string;
  messages: any;
  message: string = '';

  constructor(
    private route:ActivatedRoute,
    private chatService: ChatService,
    private chatMessageStore: Store<ChatMessageListState>
    ) { }

  ngOnInit() {
    this.token = this.route.snapshot.params['token'];
    this.chatService.getChatMessage(this.token);
    this.messages = this.chatMessageStore.select(selectChatMessageByTokenSelector(this.token));
  }

  doSubmit(){
    const data = {
      message: this.message,
      token: this.token
    }
    this.chatService.sendChatMessage(data);
    this.message = '';
  }

}
