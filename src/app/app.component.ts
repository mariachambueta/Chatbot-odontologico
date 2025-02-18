import { Component } from '@angular/core';
import { IonApp, IonRouterOutlet } from '@ionic/angular/standalone';
import { RouterModule, Routes } from '@angular/router'; // Necesitamos RouterModule

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  imports: [IonApp, IonRouterOutlet, RouterModule],
})
export class AppComponent {
  constructor() {}

  static routes: Routes = [
    {
      path: 'fivebot',
      loadComponent: () => import('./fivebot/fivebot.page').then( m => m.FIVEbotPage) //Pagina inicial
    },
    {
      path: 'ndgs',
      loadComponent: () => import('./components/ndgs/ndgs.component').then( m => m.NdgsComponent)
    },
  ];
}
