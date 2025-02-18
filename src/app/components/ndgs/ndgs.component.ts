import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonContent, IonHeader, IonTitle, IonToolbar, IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle, IonItem,  IonLabel,  IonList, IonThumbnail, IonButton } from '@ionic/angular/standalone';
@Component({
  selector: 'app-ndgs',
  templateUrl: './ndgs.component.html',
  styleUrls: ['./ndgs.component.scss'],
  imports: [IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule, IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle, IonItem,  IonLabel,  IonList, IonThumbnail, IonButton]
})
export class NdgsComponent  implements OnInit {

  constructor() { }

  ngOnInit() {}

}
