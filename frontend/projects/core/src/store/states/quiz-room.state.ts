/* author Dmitry Zharikov zdimon77@gmail.com */

import { EntityState } from '@ngrx/entity';

export interface IQuizRoomState {
    id: number;
    token: string;
    current_question: any;
}

export class QuizRoomState implements IQuizRoomState {
    constructor(
        public token: string = 'undefined',
        public current_question: any = {},
        public id: number = 0,
        ) {
    }
}

export interface QuizRoomListState extends EntityState<QuizRoomState> {

}


export const defaultState = {

};
