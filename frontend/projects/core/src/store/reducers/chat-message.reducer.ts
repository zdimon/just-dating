import {EntityAdapter, createEntityAdapter} from '@ngrx/entity';

import * as Actions from '../actions/chat-message.action';
import {ChatMessageState, ChatMessageListState, defaultState} from '../states/chat-message.state';

export const adapter: EntityAdapter<ChatMessageState> = createEntityAdapter<ChatMessageState>();

export const initialState: ChatMessageListState = adapter.getInitialState(defaultState);

export function ChatMessageReducer(state = initialState, action: Actions.ActionsUnion) {

    switch (action.type) {

        case Actions.ChatMessageActionTypes.UpdateChatMessages:

          return adapter.upsertMany(action.payload, {...state });

        default:
        return state;

    }
}
