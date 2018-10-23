# Angular

## Start
Installer NodeJS (dernière version stable) :[https://nodejs.org/en](https://nodejs.org/en)

Mouve the archive in **/opt** and extract it
```bashrc
sudo mkdir -p /opt
sudo mv /home/USER/Download/node-v8.11.1-linux-x64.tax.xz /opt
cd /opt
tar xvf node-v8.11.1-linux-x64.tax.xz
```

Add in the **~/.bashrc***
```bash
export PATH=/opt/node-v8.11.1-linux-x64/bin:$PATH
```

Reopen terminal and check the node version
```bash
node --version
```

Install angular cli with npm
```bash
npm install -g @angular/cli
```
To initialise a new projet use ng cli
```bash
ng new angular-tour-of-heroes
```
Run ti
```bash
cd angular-tour-of-heroes
ng serve --open
```

## Commandes

```ng generate component heroes```
create service  | ```ng generate service hero```
create service and register in module app | ```ng generate service hero --module=app```

## Official tutorial
Application shell :
 - link Component.attribute <-> HTML Template

The Hero Editor :
 - ng generate
 - integrate new component
 - template to diplay attribute
 - template to format with pipe
 - input [(ngModel)]

Display list :
 - *ngFor
 - (click)
 - *ngIf
 - Add style selected : [class.selected]

Master/Detail Components :
 - slice components
 - Input in child component and @Input() decorator

Services :
 - ng generate service
 - injection in the constructor argument + call in ngOnInit()
 - Async with Observable : import { Observable, of } from 'rxjs';
   - Observable<Hero[]>
   - return of(Object);
 - function anonyme/lamba (heroes => this.heroes = heroes)

Routing
 - RouterModule, Routes
 - route : path
 - <a routerLink="\heroes">.....
 - slice
 - { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
 - { path: 'detail/:id', component: HeroDetailComponent },
 - location.back();

HTTP :
 - angular-in-memory-web-api
 - 
