/* author Dmitry Zharikov zdimon77@gmail.com */

import { EntityState } from '@ngrx/entity';

export class ChatMessageState {
    id: number;
    message: string;
    owner: number;
    is_readed: boolean;
    created_at: string;
}



export interface ChatMessageListState extends EntityState<ChatMessageState> {

}


export const defaultState = {
};
