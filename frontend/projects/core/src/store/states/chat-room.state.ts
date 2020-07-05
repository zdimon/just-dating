/* author Dmitry Zharikov zdimon77@gmail.com */

import { EntityState } from '@ngrx/entity';

export interface IChatRoomState {
    id: number;
    token: string;
    abonent: number;
}

export class ChatRoomState implements IChatRoomState {
    constructor(
        public token: string = 'undefined',
        public abonent: number = 0,
        public id: number = 0,
        ) {
    }
}


export interface ChatRoomListState extends EntityState<ChatRoomState> {
    currentRoom: number | null;
}


export const defaultState = {
    currentRoom: 0
};
