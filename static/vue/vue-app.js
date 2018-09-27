

const app = new Vue(
    {
        el: '#vue-app',
        methods:
        {
            goto(refName) {
                var element = this.$refs[refName];
              console.log(element);
              var top = element.offsetTop;
              
              window.scrollTo(0, top);
            }

        },
        template: `
            <div>
            <nav class="navbar fixed-bottom" style="background-color: rgba(0,0,0,0)">
 
         
                <div class="btn-group" role="group" aria-label="Basic example">
                    <button @click="goto('GetMyFriendCode')" type="button" class="btn btn-secondary">1</button>
                    <button @click="goto('PostMessage')" type="button" class="btn btn-secondary">2</button>
                    <button @click="goto('GetAllMessages')" type="button" class="btn btn-secondary">3</button>
                    <button @click="goto('GetAllEncryptedMessages')" type="button" class="btn btn-secondary">4</button>
                    <button @click="goto('Decrypt')" type="button" class="btn btn-secondary">5</button>
                </div>
                </nav>
                <h2 ref="GetMyFriendCode">Get Your Friend Code</h2>
                <component-friend-code v-bind:name="/GetMyFriendCode/"  v-bind:head="'Get your Friend Code to share with others!'"></component-friend-code>
                <br>
                <h2 ref="PostMessage"> Post A Message To A Friend </h2>
                <component-post-message v-bind:name="/PostMessage/" v-bind:head="'Send a message to a friendly API. If you do not have any friends, try sending a message to yourself.'"></component-post-message>
                <br>
                <h2 ref="GetAllMessages"> Get All Messages</h2>
                <component-message-table v-bind:name="/GetAllMessages/" v-bind:head="'View all the messages sent to you.'"></component-message-table>
                <br>
                <h2 ref="GetAllEncryptedMessages"> Get All Encrypted Messages</h2>
                <component-message-table v-bind:name="/GetAllEncryptedMessages/" v-bind:head="'View all the messages sent to you in an encrypted form.'">></component-message-table>
                <br>
                <h2 ref="Decrypt"> Decrypt Messages Manually </h2>
                <br>
                <component-post-decrypt v-bind:name="/Decrypt/" v-bind:head="'Drop in an encrypted message from the table above to decrypt the messages manually.'"></component-post-decrypt>
              
                
            </div>           
            `
    }


)