

import { ActionReducerMap } from '@ngrx/store';

import { SessionState } from './states/session.state';
import {SessionReducer} from './reducers/session.reducer';

import { UserReducer } from './reducers/user.reducer';
import { UserListState } from './states/user.state';

import { ChatRoomListState } from './states/chat-room.state';
import { ChatRoomReducer } from './reducers/chat-room.reducer';


export interface State {
    session: SessionState;
    users: UserListState;
    chatRoom: ChatRoomListState;
}

export const reducers: ActionReducerMap<State> = {
    session: SessionReducer,
    users: UserReducer,
    chatRoom: ChatRoomReducer
  };
