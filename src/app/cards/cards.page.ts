import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonContent, IonHeader, IonTitle, IonToolbar, IonCol, IonGrid, IonRow, IonButton, IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle} from '@ionic/angular/standalone';

@Component({
  selector: 'app-cards',
  templateUrl: './cards.page.html',
  styleUrls: ['./cards.page.scss'],
  standalone: true,
  imports: [IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule, IonCol, IonGrid, IonRow, IonButton, IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle]
})
export class CardsPage implements OnInit {

  constructor() { }

  ngOnInit() {
  }
  //Tarjetas de presentación de cada uno
  tarjetas = [
    {
      titulo: "Nicolas Garcia",
      subtitulo: "Estudiante Ingenieria Multimedia",
      descripcion: "Soy estudiante de pregrado de la Universidad Militar Nueva Granada en Colombia, matriculado en el programa de Ingeniería Multimedia, donde he cursado tres años. Mi formación académica incluye un título de tecnólogo en Diseño e Integración de Automatización Mecatrónica del SENA (Servicio Nacional de Aprendizaje). Me apasiona transformar historias y objetos en entornos virtuales a través de la programación, explorar la esencia de la vida a través de las computadoras y cerrar la brecha entre el mundo virtual y el real para combinar lo mejor de ambos.",
      imagen: "/assets/NickP.png"
    },
    {
      titulo: "Valentina Vargas",
      subtitulo: "Estudiante Ingenieria Multimedia",
      descripcion: "Soy estudiante de pregrado en la Universidad Militar Nueva Granada. Mi formación académica incluye un título de tecnólogo en producción multimedia del Servicio Nacional de Aprendizaje (SENA) y actualmente estoy cursando la carrera de ingeniería multimedia, programa en el que participo desde hace tres años. Tengo un gran interés en el campo de la multimedia porque nos permite contar historias, evocar emociones y transformar la realidad a través de imágenes, sonidos y animaciones.",
      imagen: "https://static.netwrck.com/static/uploads/ai-Help-Bot-HX-Help-Bot.webp"
    },
    {
      titulo: "Maria Alejandra Chambueta",
      subtitulo: "Estudiante Ingenieria Multimedia",
      descripcion: "Soy Alejandra Chambueta, estudio Ingeniería en Multimedia en la Universidad Militar Nueva Granada. Me encanta la tecnología, el diseño y todo lo que tenga que ver con la creatividad. También me interesa el emprendimiento digital y siempre estoy buscando formas de aprender cosas nuevas y aplicar mis conocimientos en proyectos interesantes.",
      imagen: "https://static.netwrck.com/static/uploads/ai-Atza-Technology.webp"
    },
    {
      titulo: "Stefany Gelvez Quintana",
      subtitulo: "Estudiante Ingenieria Multimedia",
      descripcion: "Soy Tecnóloga en Electrónica y Comunicaciones, egresada de la Universidad Militar Nueva Granada, con disposición de aprender, aportar  lo mejor de mí, trabajar en equipo, adquirir nuevos conocimientos y habilidades. Soy una persona con características de liderazgo al progreso, proactiva, servicial y dedicada para cumplir con mis respectivos objetivos y metas, con capacidad para desarrollar proyectos en el sector de tecnología y de diseño.",
      imagen: "https://static.netwrck.com/static/uploads/ai-MD-T2-Artificial-Intelligence.webp"
    },
    {
      titulo: "Jeimmy cortes",
      subtitulo: "Estudiante Ingenieria Multimedia",
      descripcion: "Soy estudiante de Ingenieria en Multimedia de la Universidad Militar Nueva Granada. Me apasiona el diseño y lo relacionado a la tecnologia, me considero una persona que puede trabajar en equipo, con ganas de aprender continuamente y con grandes objetivos que cumplir.",
      imagen: "https://static.netwrck.com/static/uploads/ai-xerkarsa-Emotional.webp"
    }
  ];
}
