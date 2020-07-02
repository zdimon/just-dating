import { TestBed } from '@angular/core/testing';

import { WsOnlineService } from './ws-online.service';

describe('WsOnlineService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: WsOnlineService = TestBed.get(WsOnlineService);
    expect(service).toBeTruthy();
  });
});
