/* author Dmitry Zharikov zdimon77@gmail.com */

import { EntityState } from '@ngrx/entity';

export class QuizMessageState {
    id: number;
    text: string;
    user: number;
    created_at: string;
}



export interface QuizMessageListState extends EntityState<QuizMessageState> {

}


export const defaultState = {
};
