import { ComponentFixture, TestBed } from '@angular/core/testing';
import { FIVEbotPage } from './fivebot.page';

describe('FIVEbotPage', () => {
  let component: FIVEbotPage;
  let fixture: ComponentFixture<FIVEbotPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(FIVEbotPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
