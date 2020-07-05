import { Observable } from 'rxjs';
import { Component, OnInit } from '@angular/core';

// Store
import { Store } from '@ngrx/store';
import * as userActions from './../../../../../core/src/store/actions/user.action';
import { UserState, UserListState } from './../../../../../core/src/store/states/user.state';
import { selectUsersArray } from './../../../../../core/src/store/selectors/user.selector';

// Service
import { ApiService } from './../../../../../core/src/lib/services/api.service';
import { ChatService } from './../../../../../core/src/lib/services/chat.service';


@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.scss']
})
export class IndexComponent implements OnInit {

  users: Observable<UserState[]>;

  constructor(
    private userStore: Store<UserListState>,
    private api: ApiService,
    private chatService: ChatService

  ) {
    this.api.getUserList().subscribe(data => {
        this.userStore.dispatch(new userActions.UpdateUsers(data));
    });
    this.users = this.userStore.select(selectUsersArray);
   }

  ngOnInit() {
  }

  doCallToChat(userId: number) {
    this.chatService.getChatRoom(userId);
  }
}
