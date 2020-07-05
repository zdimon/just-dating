import {EntityAdapter, createEntityAdapter} from '@ngrx/entity';

import * as Actions from '../actions/chat-room.action';
import {ChatRoomState, ChatRoomListState, defaultState} from '../states/chat-room.state';

export const adapter: EntityAdapter<ChatRoomState> = createEntityAdapter<ChatRoomState>();

export const initialState: ChatRoomListState = adapter.getInitialState(defaultState);

export function ChatRoomReducer(state = initialState, action: Actions.ActionsUnion) {

    switch (action.type) {

        case Actions.ChatRoomActionTypes.UpdateChatRoom:

          return adapter.upsertOne(action.payload, {...state, currentRoom: action.payload.id});

        default:
        return state;

    }
}
