import { ChatMessageListState, ChatMessageState } from '../states/chat-message.state';
import { createSelector, createFeatureSelector } from '@ngrx/store';

export const getChatMessageListStateSelector = createFeatureSelector<ChatMessageListState>('chatMessage');

export const selectChatMessageIdsSelector = createSelector(
       getChatMessageListStateSelector, 
       (state: ChatMessageListState) => state.ids
);

export const selectChatMessageObjectsSelector = createSelector(
    getChatMessageListStateSelector,
    (state: ChatMessageListState) => state.entities
);

export const selectChatMessageArraySelector = createSelector(
    selectChatMessageIdsSelector,
    selectChatMessageObjectsSelector,
    (ids: any, objects: any) => ids.map( id => objects[id])
);

export const selectChatMessageByTokenSelector = (token: string) => createSelector(
    selectChatMessageArraySelector,
    (messages: any) => messages.filter((item) => item.token === token)
);

