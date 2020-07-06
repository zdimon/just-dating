
import { Component, OnInit, Input } from '@angular/core';
import { UserState } from './../../../store/states/user.state';

@Component({
  selector: 'core-avatar',
  templateUrl: './avatar.component.html',
  styleUrls: ['./avatar.component.scss']
})
export class AvatarComponent implements OnInit {

  @Input() user: UserState;

  constructor() { }

  ngOnInit() {
  }

}
