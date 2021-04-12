import { Action } from '@ngrx/store';
import { QuizRoomState } from './../states/quiz-room.state';

export enum QuizRoomActionTypes {
    UpdateQuizRoom = '[Quiz Room] update room'
}

export class UpdateQuizRoom implements Action {
    readonly type = QuizRoomActionTypes.UpdateQuizRoom;
    constructor(public payload: QuizRoomState) {}
  }

export type ActionsUnion = UpdateQuizRoom;
