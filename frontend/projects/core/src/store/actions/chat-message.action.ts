import { Action } from '@ngrx/store';
import { ChatMessageState } from './../states/chat-message.state';

export enum ChatMessageActionTypes {
    UpdateChatMessages = '[Chat Message] add/update messages'
}

export class UpdateChatMessages implements Action {
    readonly type = ChatMessageActionTypes.UpdateChatMessages;
    constructor(public payload: ChatMessageState[]) {}
  }

export type ActionsUnion = UpdateChatMessages;
