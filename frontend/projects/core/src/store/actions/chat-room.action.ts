import { Action } from '@ngrx/store';
import { ChatRoomState } from './../states/chat-room.state';

export enum ChatRoomActionTypes {
    UpdateChatRoom = '[Chat Room] update room'
}

export class UpdateChatRoom implements Action {
    readonly type = ChatRoomActionTypes.UpdateChatRoom;
    constructor(public payload: ChatRoomState) {}
  }

export type ActionsUnion = UpdateChatRoom;
