import { Action } from '@ngrx/store';
import { QuizMessageState } from './../states/quiz-message.state';

export enum QuizMessageActionTypes {
    UpdateQuizMessages = '[Quiz Message] add/update messages',
    UpdateQuizMessage = '[Quiz Message] add/update one message'
}

export class UpdateQuizMessages implements Action {
    readonly type = QuizMessageActionTypes.UpdateQuizMessages;
    constructor(public payload: QuizMessageState[]) {}
  }

  export class UpdateQuizMessage implements Action {
    readonly type = QuizMessageActionTypes.UpdateQuizMessage;
    constructor(public payload:QuizMessageState) {}
  }

export type ActionsUnion = UpdateQuizMessages | UpdateQuizMessage;
