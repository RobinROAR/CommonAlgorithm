#include <stdlib.h>
#include <stdio.h>



#include<stdio.h>
#include<stdlib.h>


typedef struct node{
	int num;
	int data;
	node *next;
}node;

//建立链表，两个指针，p新建节点，q链接前后节点
node *create(int n){
	node *head,*q,*p;
	for(int i=0;i<n;i++){
		p = (node*)malloc(sizeof(node));
		printf("Please input node%d : ", i+1);
		scanf("%d,%d",&p->num,&p->data);
		if(i==0){
			q =p;
			head = p;
			}
			else{
				q->next = p;
				p->next = NULL;
				q = p;
			}
		}
	return head;
}

//释放链表， 两个指针，q删除释放当前节点，p指向下一个
void  drop(node *head){
	node *p,*q;
	if(head = NULL){printf("No link");exit(0);}
	p = q =head;
	while(p!=NULL){
		p=p->next;
		free(q);
		q=p;
	}
	
	if(p == NULL and q == NULL) printf("drop ok \n") ;
	else printf("wrong");
	
}	
		
//展示链表，一个指针
void show(node *head){
	node *p;
	p = head;
	while(p!=NULL){
		printf("num : %d ,data : %d \n", p->num,p->data);
		p = p->next;
	}
}

//插入链表
void insert(node *head,int n,int data){
	node *p,*q;
	p = head;
	int i;
	for(i=0;i<n;i++){
		p = p->next;
	}
	q = (node*)malloc(sizeof(node));
	printf("Please input data after node%d: ", n)
	scanf("%d,%d",&q->num,&q->data)
	q->next = p->next;
	p->next = q;
}
	
	
int main(){
	printf("Please input the len of linknode: ");
	int n;
	scanf("%d", &n);
	node *head = create(n);
	show(head);
	drop(head);
	
	scanf("%d", &n);
	return 0;	
	
	
}
