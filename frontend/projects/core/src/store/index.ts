

import { ActionReducerMap } from '@ngrx/store';

import { SessionState } from './states/session.state';
import {SessionReducer} from './reducers/session.reducer';

import { UserReducer } from './reducers/user.reducer';
import { UserListState } from './states/user.state';

import { ChatRoomListState } from './states/chat-room.state';
import { ChatRoomReducer } from './reducers/chat-room.reducer';

import { ChatMessageListState } from './states/chat-message.state';
import { ChatMessageReducer } from './reducers/chat-message.reducer';

import { QuizRoomListState } from './states/quiz-room.state';
import { QuizRoomReducer } from './reducers/quiz-room.reducer';


export interface State {
    session: SessionState;
    users: UserListState;
    chatRoom: ChatRoomListState;
    chatMessage: ChatMessageListState;
    quizRoom: QuizRoomListState;
}

export const reducers: ActionReducerMap<State> = {
    session: SessionReducer,
    users: UserReducer,
    chatRoom: ChatRoomReducer,
    chatMessage: ChatMessageReducer,
    quizRoom: QuizRoomReducer
  };
