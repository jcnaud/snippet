# HttpClientInMemoryWebApiModule

This module all to simulate a real external API.
This modiel intercept Http request message and reply.
This transparent for the angular app even if this module is installer and confugurer on it

## Requirements
REQUIRE HttpClient module FIRST !!!


## Install 
Install the module with npm
```bash
npm install angular-in-memory-web-api --save
```

On **src/app/app.module.ts ** add :
```ts
import { HttpClientInMemoryWebApiModule } from 'angular-in-memory-web-api';
import { InMemoryDataService }  from './in-memory-data.service';

@NgModule({
  ...
  imports: [
    ...
    // Put HttpClientInMemoryWebApiModule AFTER THE HttpClientModule !!.
    // Remove it when a real server is ready to receive requests.
    HttpClientInMemoryWebApiModule.forRoot(
    InMemoryDataService, { dataEncapsulation: false }
  ],
  ...
})
```

## Service

Create the service
On src/app/in-memory-data.service.ts add :
```ts
import { InMemoryDbService } from 'angular-in-memory-web-api';

export class InMemoryDataService implements InMemoryDbService {
  createDb() {
    const heroes = [
      { id: 11, name: 'Mr. Nice' },
      { id: 12, name: 'Narco' },
      { id: 13, name: 'Bombasto' },
      { id: 14, name: 'Celeritas' },
      { id: 15, name: 'Magneta' },
      { id: 16, name: 'RubberMan' },
      { id: 17, name: 'Dynama' },
      { id: 18, name: 'Dr IQ' },
      { id: 19, name: 'Magma' },
      { id: 20, name: 'Tornado' }
    ];
    return {heroes};
  }
}
```